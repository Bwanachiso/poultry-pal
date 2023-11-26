import ChatBot from "react-simple-chatbot";

const Home = () => (
  <ChatBot
    steps={[
      {
        id: "1",
        message:
          "Hello! Welcome to the Poultry Farm ChatBot. What is your name?",
        trigger: "2",
      },
      {
        id: "2",
        user: true,
        trigger: "3",
      },
      {
        id: "3",
        message:
          "Hi {previousValue}, nice to meet you! Are you interested in poultry farming?",
        trigger: "4",
      },
      {
        id: "4",
        user: true,
        trigger: "5",
      },
      {
        id: "5",
        message:
          "That's great! Poultry farming involves raising chickens, ducks, or other birds for meat or eggs. Do you have any specific questions about poultry farming?",
        trigger: "6",
      },
      {
        id: "6",
        user: true,
        trigger: "7",
      },
      {
        id: "7",
        message: `Feel free to ask any questions you have. Whether it's about choosing the right breeds, setting up a coop, or managing the health of your poultry, I'm here to help!`,
        end: true,
      },
    ]}
  />
);

export default Home;
