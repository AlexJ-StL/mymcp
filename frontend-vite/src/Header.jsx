import React from 'react';
import './Header.css'; // We'll create this CSS file next

function Header() {
  return (
    <header className="app-header">
      <h1 className="app-title">MyMCP Chef</h1>
      <p className="app-tagline">Delivering Delectable MCP Dishes for Developers</p>
    </header>
  );
}

export default Header;