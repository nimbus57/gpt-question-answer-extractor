// minified version for the bookmarklet
//javascript:(function(){function downloadData(data,filename){let blob=new Blob([data],{type:'text/plain'});let link=document.createElement('a');link.href=URL.createObjectURL(blob);link.download=filename;document.body.appendChild(link);link.click();document.body.removeChild(link);}let articles=[...document.querySelectorAll('article')].map(el=>el.innerText);let pairs=[];for(let i=0;i<articles.length-1;i+=2){pairs.push([articles[i],articles[i+1]]);}let sessionName=[...document.querySelectorAll('li[data-testid|="history-item"]')].find(el=>el.firstChild.classList.contains('bg-token-sidebar-surface-secondary')).innerText;downloadData(JSON.stringify({[sessionName]:pairs},undefined,4),'articles.json');})();

// get all of the article nodes; the questions and answers are pairwise in this list, so indexes: (0,1), (2,3), etc...
(function() {
    function downloadData(data, filename) {
        let blob = new Blob([data], { type: 'text/plain' });
        let link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }

    // Get all article elements and process their inner text
    let articles = [...document.querySelectorAll('article')].map(el => el.innerText);

    // Pair the inner texts
    let pairs = [];
    console.log("Total number of pairs: ", articles.length / 2)
    for (let i = 0; i < articles.length - 1; i += 2) {
        pairs.push([articles[i], articles[i + 1]]);
    }

    // Download the pairs as a text file
    let sessionName = [...document.querySelectorAll('li[data-testid|="history-item"]')].find(el => el.firstChild.classList.contains('bg-token-sidebar-surface-secondary')).innerText;
    downloadData(JSON.stringify({[sessionName]: pairs}, undefined, 4), 'articles.json');
})();
