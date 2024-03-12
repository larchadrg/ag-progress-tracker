const userCardTemplate = document.querySelector("[data-user-template]")
const userCardContainer = document.querySelector("[data-user-cards-container]")
const searchInput = document.querySelector("[data-search]")

searchInput.addEventListener("input", filterCharacters);
getCharactersInfo();

function filterCharacters() {
  let inputValue = searchInput.value.toLowerCase();
  let factions = activeFilters("region");
  let elements = activeFilters("element");
  let progress = activeFilters("progress");

  characters.forEach(character => {
    let isVisible = true; 
    if (inputValue.length > 0) {
      isVisible = character.name.toLowerCase().startsWith(inputValue) || character.model.toLowerCase().startsWith(inputValue);
    }
    if (factions.length > 0){
      isVisible = isVisible && factions.includes(character.faction);
    }
    if (elements.length > 0){
      //checks if has at least one element from the charcter
      isVisible = isVisible && elements.some(element => character.elem.includes(element));
    }
    if (progress.length > 0){
      isVisible = isVisible && progress.includes(document.getElementById("select-progress-" + character.id).value);
    }
      character.element.style.display = isVisible ? "flex" : "none"; 
  })
}

function activeFilters(category){
  let cbs = Array.from(document.querySelectorAll('input[cb-filter-option-' + category + ']:checked'));
  let filters = cbs.map(cb => cb.value);
  return filters;
}

function getCharactersInfo(){
  fetch("api/characters-info")
  .then(res => res.json())
  .then(data => {
    characters = data.map(character => {
      const card = userCardTemplate.content.cloneNode(true).children[0]
      const header = card.querySelector("[data-header]")
      const image = card.querySelector("[data-image]")
      const model = card.querySelector("[data-model]")
      const rank = card.querySelector("[data-rank]")
      const element = card.querySelector("[data-element]")
      const faction = card.querySelector("[data-faction]")
      const characterId = card.querySelector("[data-id]")
      const select = card.querySelector("[data-select]")
      const check = card.querySelector("[data-check]")

      characterId.id = character.id
      header.textContent = character.name
      image.src = image.src + character.image
      model.textContent = character.model
      rank.textContent = rank.textContent + character.rank
      element.textContent = element.textContent + character.elements
      faction.textContent = faction.textContent + character.genzone
      select.id = select.id + character.id
      check.id = check.id + character.id
      check.href = check.href + character.id
      userCardContainer.append(card)
      return {
        name: character.name,
        id: character.id,
        faction: character.genzone,
        model: character.model,
        rank: character.rank,
        elem: character.elements, 
        element: card
      }
    })
  })
  .then(() => {
    loadCharacterStatus();
    })
  }

// save card background color
function changeCharacterStatus(element){
  let characterStatusAll = {};
  if (localStorage.getItem('characterStatusAll')) {
    characterStatusAll = JSON.parse(localStorage.getItem('characterStatusAll'));
  }
  let id = element.closest(".card").querySelector("[data-id]").id;
  const status = element.value;
  characterStatusAll[id] = status;
  localStorage.setItem('characterStatusAll', JSON.stringify(characterStatusAll));
  changeBgCard(element);
}

async function loadCharacterStatus(){
  let characterStatusAll = {}
  if (localStorage.getItem('characterStatusAll')) {
    characterStatusAll = JSON.parse(localStorage.getItem('characterStatusAll'));
  }
  characters.forEach(character => {
    let id = character.id; 
    if (id in characterStatusAll){
      document.getElementById("select-progress-" + id).value = characterStatusAll[id];
    }
    changeBgCard(document.getElementById("select-progress-" + id));
  })
}

function changeBgCard(element){
  //change background color of card by its select value 
  var selectedValue = element.options[element.selectedIndex].value;
  var card = element.closest('.card');

  switch (selectedValue) {
    case "Not Started":
      card.style.backgroundColor = "lightgray";
      break;
    case "In Progress":
        card.style.backgroundColor = "khaki";
        break;
    case "Completed":
      card.style.backgroundColor = "lightgreen";
      break;
    default:
      element.options[element.selectedIndex].value = "Not Started";
      card.style.backgroundColor = "lightgray";
      break;
  }
}