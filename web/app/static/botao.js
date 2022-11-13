async function adiciona(botao) {

    let res = await fetch('/botao', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        
        body: '{"command": "' + botao + '"}',
    });

    if (res.ok) {

        // let text = await res.text();
        // return text;

        let ret = await res.json();
        console.log(ret.Code);
        if (ret.Code == 500){
            alert("limite atingido");
        } else {
            window.location.reload();
        }

    } else {
        return `HTTP error: ${res.status}`;
    }
}