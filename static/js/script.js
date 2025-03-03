document.addEventListener('DOMContentLoaded', function() {
    const queryForm = document.getElementById('query-form');
    const promptInput = document.getElementById('prompt-input');
    const submitBtn = document.getElementById('submit-btn');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    const chatgptResponse = document.getElementById('chatgpt-response');
    const claudeResponse = document.getElementById('claude-response');
    
    // Funzione per gestire l'invio del form
    queryForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const prompt = promptInput.value.trim();
        if (!prompt) {
            alert('Per favore, inserisci una domanda');
            return;
        }
        
        // Mostra il loading spinner
        results.style.display = 'none';
        loading.style.display = 'block';
        submitBtn.disabled = true;
        
        try {
            // Invia la richiesta al server
            const response = await fetch('/query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt: prompt })
            });
            
            if (!response.ok) {
                throw new Error('Errore nella richiesta');
            }
            
            const data = await response.json();
            
            // Visualizza i risultati
            chatgptResponse.innerHTML = formatText(data.chatgpt);
            claudeResponse.innerHTML = formatText(data.claude);
            
            // Nascondi loading e mostra risultati
            loading.style.display = 'none';
            results.style.display = 'grid';
        } catch (error) {
            console.error('Errore:', error);
            alert('Si è verificato un errore durante l\'elaborazione della richiesta');
            loading.style.display = 'none';
        } finally {
            submitBtn.disabled = false;
        }
    });
    
    // Funzione per formattare il testo (supporta markdown base)
    function formatText(text) {
        if (!text) return '';
        
        // Converti markdown in HTML (implementazione base)
        // Converti i blocchi di codice ```
        text = text.replace(/```(\w+)?\n([\s\S]*?)\n```/g, '<pre><code>$2</code></pre>');
        
        // Converti **bold**
        text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        
        // Converti *italic*
        text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
        
        // Converti newlines in <br>
        text = text.replace(/\n/g, '<br>');
        
        return text;
    }
});
