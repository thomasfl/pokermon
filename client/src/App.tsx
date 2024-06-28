import "./App.css";
import { AddPlayer } from "./pokermon/AddPlayer";
import { Users } from "./pokermon/Users";

function App() {

  return (
    <>
      <h1>Pokérmon Poker</h1>
      <div className="card">
        <AddPlayer/>
        <br/>
        <Users />
      </div>
    </>
  );
}

export default App;
