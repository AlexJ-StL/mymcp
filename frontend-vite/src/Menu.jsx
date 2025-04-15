import React from 'react';
import './Menu.css'; // CSS file to be created next

// Placeholder examples - these could come from props or state later
const menuItems = [
  { id: 'basic_web', title: 'Simple Web Server', description: 'A basic Python Flask server serving a static HTML page.' },
  { id: 'data_api', title: 'Data Fetching API', description: 'An MCP server that fetches data from a public API (e.g., weather).' },
  { id: 'file_processor', title: 'File Processor', description: 'An MCP tool that reads a text file and counts word frequency.' },
];

// The 'onSelect' prop will be passed down from App.jsx later
// to handle populating the prompt when an item is clicked.
function Menu({ onSelect }) {
  return (
    <section className="menu-section">
      <h2 className="section-title">MCP Menu</h2>
      <p className="menu-description">Need inspiration? Select a starter dish:</p>
      <div className="menu-items-container">
        {menuItems.map((item) => (
          <button
            key={item.id}
            className="menu-item"
            onClick={() => onSelect(item.description)} // Pass description as example prompt
            title={`Use prompt: "${item.description}"`}
          >
            <h3 className="menu-item-title">{item.title}</h3>
            {/* <p className="menu-item-description">{item.description}</p> */}
          </button>
        ))}
      </div>
    </section>
  );
}

export default Menu;