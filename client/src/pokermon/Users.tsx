import { useState, useEffect } from "react";

interface User {
    username: string;
}

export const Users = () => {
  const [users, setUsers] = useState<User[]>([]);

  const fetchusers = async () => {
    try {
      const url: string = "http://localhost:8000/user/users";
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const result = await response.json();
      setUsers(result);
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  useEffect(() => {
    fetchusers();
  }, []);

  return (
    <div>
      <b>Current players</b>
      <ul>{users && users.map((user, index) => 
        <li key={index}>{user.username}</li>)}
        </ul>
    </div>
  );
};
