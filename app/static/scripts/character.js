const currentRankSelector = document.querySelector('.character.personal_rank.selector');
const characterId = document.querySelector('.characterId').textContent;
const weaponLevel = document.querySelector('.weapon.level.selector');

function storeWeaponLevel(){
    const level = weaponLevel.value;
    localStorage.setItem('weaponLevel'+characterId, level);
}
function loadWeaponLevel(){
    const savedLevel = localStorage.getItem('weaponLevel'+characterId);
    if (savedLevel){
        weaponLevel.value = savedLevel;
    }
}
weaponLevel.addEventListener('input', () => {
    storeWeaponLevel();
});

function loadRank(){
    const savedRank = localStorage.getItem('rank'+characterId); 
    if (savedRank){
        currentRankSelector.value = savedRank; 
    } else {
        const initialRank = document.querySelector('.character.rank').textContent;
        currentRankSelector.value = initialRank;
    }
}

function storeRank(elem){
    const rank = elem.value;
    localStorage.setItem('rank'+characterId, rank);
}

currentRankSelector.addEventListener('input', (e) => {
    storeRank(e.target);
});

function loadSkillsLevels(){
    const savedSkillsLevels = JSON.parse(localStorage.getItem('skillsLevels'+characterId));
    if (savedSkillsLevels){
        const skillsLevels = document.querySelectorAll('.skill.level.selector');
        for (let i=0; i < skillsLevels.length; i++){
            skillsLevels[i].value = savedSkillsLevels[i];
        }
    }
}

const skillsLevels = document.querySelectorAll('.skill.level.selector');
function storeSkillsLevels(){
    let skillsLevelsArray = [];
    for (let i=0; i < skillsLevels.length; i++){
        skillsLevelsArray.push(skillsLevels[i].value);
    }
    localStorage.setItem('skillsLevels'+characterId, JSON.stringify(skillsLevelsArray));
}


for (let i=0; i < skillsLevels.length; i++){
    skillsLevels[i].addEventListener('input', () => {
        storeSkillsLevels();
    });
}


const sigilsLevels = document.querySelectorAll('.sigil.level.selector');

function storeSigilsLevel(){
    let sigilsLevelsArray = [];
    for (let i=0; i < sigilsLevels.length; i++){
        sigilsLevelsArray.push(sigilsLevels[i].value);
    }
    localStorage.setItem('sigilsLevels'+characterId, JSON.stringify(sigilsLevelsArray));
}

function loadSigilsLevels(){
    const savedSigilsLevels = JSON.parse(localStorage.getItem('sigilsLevels'+characterId));
    if (savedSigilsLevels){
        for (let i=0; i < sigilsLevels.length; i++){
            sigilsLevels[i].value = savedSigilsLevels[i];
        }
    }
}

sigilsLevels.forEach((elem) => {
    elem.addEventListener('input', () => {
        storeSigilsLevel();
    });
});

function loadData(){
    loadRank();
    loadSkillsLevels();
    loadSigilsLevels();
    loadWeaponLevel();
}
loadData();

//TODO: LOAD WARP EFFECT LEVELS AND NAMES FROM LOCAL STORAGE