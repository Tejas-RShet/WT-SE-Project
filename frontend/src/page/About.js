import React from "react";
import "./About.css"; // Ensure this file is created and imported

const About = () => {
  const teammates = [
    { name: "Anish", role: "01FE22BCS240" },
    { name: "Aakash", role: "01FE22BCS133" },
    { name: "Tejas", role: "01FE22BCS231" },
    { name: "Atharva", role: "01FE23BCS402" },
    { name: "Prajwal", role: "01FE23BCS409" },
    { name: "Vijaykumar", role: "01FE22BCS402" },
    { name: "Mubashar", role: "01FE23BCS417" },
  ];

  return (
    <div className="about-container">
      <h1>About Us </h1>

      <h1>Teammates</h1>
      <ul className="teammates-list">
        {teammates.map((teammate, index) => (
          <li key={index} className="teammate-item">
            <strong>{teammate.name}</strong> - {teammate.role}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default About;
