const userCardTemplate = document.querySelector("[data-user-template]")
const userCardContainer = document.querySelector("[data-user-cards-container]")
const searchInput = document.querySelector("[data-search]")

let users = []

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
      console.log(card)

      header.textContent = character.name
      image.src = image.src + character.image
      model.textContent = character.model
      rank.textContent = character.rank
      element.textContent = character.element
      faction.textContent = character.faction
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