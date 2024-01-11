const userCardTemplate = document.querySelector("[data-user-template]")
const userCardContainer = document.querySelector("[data-user-cards-container]")
const searchInput = document.querySelector("[data-search]")

searchInput.addEventListener("input", filterCharacters);

function filterCharacters() {
  let inputValue = searchInput.value.toLowerCase();
  let factions = activeRegions();
  let elements = activeElements();

  characters.forEach(character => {
    let isVisible = true; 
    if (inputValue.length > 0) {
      isVisible = character.name.toLowerCase().startsWith(inputValue) || character.model.toLowerCase().startsWith(inputValue);
    }
    if (factions.length > 0){
      isVisible = isVisible && factions.includes(character.faction);
    }
    if (elements.length > 0){
      isVisible = isVisible && elements.includes(character.elem);
    }
      character.element.style.display = isVisible ? "flex" : "none"; 
  })
}

function activeRegions(){
  let cbs = Array.from(document.querySelectorAll('input[cb-filter-option-region]:checked'));
  let regions = cbs.map(cb => cb.value);
  return regions;
}

function activeElements(){
  let cbs = Array.from(document.querySelectorAll('input[cb-filter-option-element]:checked'));
  let elements = cbs.map(cb => cb.value);
  return elements;
}

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
      element.textContent = element.textContent + character.element
      faction.textContent = faction.textContent + character.genzone
      select.id = select.id + character.id
      check.id = check.id + character.id
      check.href = check.href + character.id
      userCardContainer.append(card)
      return {
        name: character.name,
        faction: character.genzone,
        model: character.model,
        rank: character.rank,
        elem: character.element, 
        element: card
      }
    })
  })

function changeBgCard(element, cardClass){
  //change background color of card by its select value 
  var selectedValue = element.options[element.selectedIndex].value;
  var card = element.closest('.card');

  switch (selectedValue) {
    case "not_started":
      card.style.backgroundColor = "lightgray";
      card.classList.add(cardClass); // Agregar la clase
      break;
    case "finished":
      card.style.backgroundColor = "lightgreen";
      card.classList.remove(cardClass); // Quitar la clase
      break;
    default:
      // Puedes manejar otros valores si es necesario
      card.style.backgroundColor = ""; // Restaurar el color por defecto
      card.classList.remove(cardClass); // Quitar la clase
      break;
  }

}