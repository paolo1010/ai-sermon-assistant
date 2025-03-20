import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import './App.css';

function App() {
  const [topic, setTopic] = useState('');
  const [outline, setOutline] = useState('');
  const [language, setLanguage] = useState('');

  const handleGenerate = async () => {
    // 🔹 Check if topic is empty before generating
    if (!topic.trim()) {
      alert("Please enter a sermon topic before generating.");
      return;
    }

    setOutline("Generating...");
    setLanguage('');

    try {
      const response = await fetch('http://127.0.0.1:8000/generate-outline', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic })
      });

      const data = await response.json();
      console.log("API Response:", data);
      setOutline(data.outline || "No outline generated.");
      setLanguage(data.language || "Unknown Language");
    } catch (error) {
      console.error("Error fetching sermon:", error);
      setOutline("Failed to generate sermon. Check console for details.");
    }
  };

  // 🔹 Function to clear input and output
  const handleClear = () => {
    setTopic('');
    setOutline('');
    setLanguage('');
  };

  return (
    <div className="App">
      <h1>📖 AI Sermon Assistant</h1>
      {/* 🔹 Description Section */}
      <div className="description">
        <p>
          <strong>What is this tool?</strong><br/>  
          The AI Sermon Assistant is a powerful tool designed to help pastors, preachers, and Bible teachers generate structured sermon outlines based on any topic.  
        </p>
        <p>
          <strong>How to use it?</strong><br/>
          1️⃣ Enter a sermon topic (e.g., "Faith in God").<br/>  
          2️⃣ Click the <strong>Generate Sermon Outline</strong> button.<br/>  
          3️⃣ The AI will detect the language, format the sermon, and provide relevant Bible verses.<br/>  
          4️⃣ If needed, click <strong>Clear</strong> to start over.  
        </p>
      </div>

      <textarea
        placeholder="Enter sermon topic..."
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />
      <button onClick={handleGenerate}>Generate Sermon Outline</button>

      <div className="result">
        {language && <h3>🗣️ Sermon Language: {language}</h3>}
        <ReactMarkdown remarkPlugins={[remarkGfm]}>{outline}</ReactMarkdown>
      </div>

      {/* 🔹 Move "Clear" button below the result */}
      {outline && (
        <button onClick={handleClear} className="clear-button">Clear</button>
      )}
    </div>
  );
}

export default App;