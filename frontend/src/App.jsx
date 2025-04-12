import { useState } from 'react';
import axios from 'axios';

function App() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState(null);

  const handleClick = async () => {
    try {
      const res = await axios.get(`http://127.0.0.1:5000/api/${input}`);
      setResponse(JSON.stringify(res.data));
    } catch (error) {
      console.error("Error fetching:", error);
      setResponse("Something went wrong");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <input
        type="text"
        placeholder="Type something..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        style={{ padding: "0.5rem", fontSize: "1rem" }}
      />
      <button onClick={handleClick} style={{ marginLeft: "1rem" }}>
        Send to Flask
      </button>
      {response && <p>Flask says: <strong>{response}</strong></p>}
    </div>
  );
}

export default App;