import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [prompt, setPrompt] = useState('');
  const [code, setCode] = useState('');

  const generateCode = async () => {
    const form = new FormData();
    form.append('prompt', prompt);
    const res = await axios.post('http://localhost:8000/generate/', form);
    setCode(res.data.code);
  };

  return (
    <div style={{ padding: 40, fontFamily: 'Arial, sans-serif' }}>
      <h1>🧠 AI Website Generator</h1>
      <textarea
        placeholder="Describe your website (e.g., I want an ecommerce site)..."
        rows="6"
        style={{ width: '100%', padding: 10 }}
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <br />
      <button
        onClick={generateCode}
        style={{ marginTop: 10, padding: '10px 20px', fontWeight: 'bold' }}
      >
        Generate Website Code
      </button>

      <h2 style={{ marginTop: 40 }}>Generated Code:</h2>
      <pre
        style={{
          background: '#f5f5f5',
          padding: 20,
          whiteSpace: 'pre-wrap',
          maxHeight: 500,
          overflowY: 'auto',
        }}
      >
        {code}
      </pre>
    </div>
  );
}

export default App;
