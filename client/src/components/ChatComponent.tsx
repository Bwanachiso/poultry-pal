// ChatComponent.tsx
import{ useState, useEffect } from 'react';
import axios from 'axios';

const ChatComponent: React.FC = () => {
  const [userMessage, setUserMessage] = useState('');
  const [chatHistory, setChatHistory] = useState<string[]>([]);

  const sendMessage = async () => {
    if (!userMessage) return;

    try {
      // Send user message to the Flask API
      const response = await axios.post('http://127.0.0.1:5000/api/chat', { message: userMessage });
      const botReply = response.data.message;

      // Update chat history
      setChatHistory([...chatHistory, `You: ${userMessage}`, `Bot: ${botReply}`]);

      // Clear the input field
      setUserMessage('');
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  useEffect(() => {
    // Initialize the conversation with a greeting message
    setChatHistory(['Bot: Hello! How can I assist you today?']);
  }, []);

  return (
    <div>
      <div className="chat-history">
        {chatHistory.map((message, index) => (
          <div key={index}>{message}</div>
        ))}
      </div>
      <input
        type="text"
        value={userMessage}
        onChange={(e) => setUserMessage(e.target.value)}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default ChatComponent;
