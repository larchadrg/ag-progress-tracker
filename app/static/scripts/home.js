const userCardTemplate = document.querySelector("[data-user-template]")
const userCardContainer = document.querySelector("[data-user-cards-container]")
const searchInput = document.querySelector("[data-search]")

searchInput.addEventListener("input", e => {
  const value = e.target.value.toLowerCase()
  characters.forEach(character => {
    const isVisible = character.name.toLowerCase().includes(value) || character.model.toLowerCase().includes(value);
      character.element.classList.toggle("hide", !isVisible)
  })
})

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