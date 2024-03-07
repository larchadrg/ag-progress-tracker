function storeBackup(){
    const localStorageItems = retrieveLocalStorageItems();
    const jsonString = JSON.stringify(localStorageItems, null, 2);
    // Create a Blob containing the JSON string
    const blob = new Blob([jsonString], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "AGBackupData.json";
    // Append the link to the document body and click it to trigger the download
    document.body.appendChild(a);
    a.click();
    // Clean up by removing the link
    document.body.removeChild(a);
}

function retrieveLocalStorageItems(){
    const localStorageItems = {};
    for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        const value = localStorage.getItem(key);
        localStorageItems[key] = value;
    }
return localStorageItems;
}

function restoreBackup(){
    const input = document.createElement("input");
    input.type = "file";
    input.accept = "application/json";
    input.click();
    input.onchange = function () {
        const file = input.files[0];
        const reader = new FileReader();
        reader.readAsText(file, "UTF-8");
        reader.onload = function () {
            const localStorageItems = JSON.parse(reader.result);
            for (const key in localStorageItems) {
                localStorage.setItem(key, localStorageItems[key]);
            }
            location.reload();
        };
    };
}