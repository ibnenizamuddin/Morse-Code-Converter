async function getMorseCode() {
    const MorseInput = document.getElementById('MorseTextInput');
    const MorseOutput = document.getElementById('MorseTextOutput');
    const apiUrl = '/result?value=' + MorseInput.value;
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        console.log(data);
        console.log(data.morsecode);

        MorseOutput.value = data.morsecode;

    } catch (error) {

    }

}