import { useState } from "react";
import { useLocalStorage } from "usehooks-ts";

export const AddPlayer = () => {
  const [game, setGame] = useState<any>();
  const [playerName, setPlayerName] = useLocalStorage<string>("playerName", "");
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setPlayerName(e.target.value);
  };

  const startNameGame = async () => {
    try {
      const url: string = "http://localhost:8000/game/game";
      const response = await fetch(url, {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: "POST",
        body: JSON.stringify({player: "Thomas", name: "Family Poker"})
    });
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const result = await response.json();
      setGame(result);
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Navn"
        onChange={handleInputChange}
        value={playerName}
      />
      <br />
      <br />
      Name: {playerName}
      <br />
      <pre>{JSON.stringify(game)}</pre>
      <br/>
      <button onClick={startNameGame}>Start new game</button>
    </div>
  );
};
