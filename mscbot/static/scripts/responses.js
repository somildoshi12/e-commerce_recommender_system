function getBotResponse(input) {
    // Simple responses
    if (input.includes("hello") == true) {
        return "Hello there!";
    } 
    else if (input.includes("goodbye") == true) {
        return "Talk to you later!";
    } 
    else if (input.includes("commerce college") == true) {
        return "Best colleges in mumbai are : 'NM College','Mithibai College','NL College'";
    }
    else if (input.includes("science college") == true) {
        return "Best colleges in mumbai are : 'Mithibai College','Jai Hind','Elphinstone College'";
    }
    else if (input.includes("arts college") == true) {
        return "Best colleges in mumbai are : 'St. Xavier's College','Jai Hind','K.J. Somaiya College Of Arts And Commerce'";
    }
    else {
        return "Try asking something else!";
    }
}