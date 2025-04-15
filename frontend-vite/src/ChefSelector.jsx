import React from 'react';
import './ChefSelector.css'; // CSS file to be created next

// For now, this component just displays the default chef.
// Later, it can be updated with state and a dropdown/radio buttons
// when multiple chefs and API support are available.
function ChefSelector() {
  const currentChef = "Google Gemini 2.5 Pro Exp 0325"; // Default/only chef for now

  return (
    <section className="chef-selector-section">
      <h2 className="section-title">Pick Your Chef</h2>
      <div className="chef-display">
        <span className="chef-label">Current Chef:</span>
        <span className="chef-name">{currentChef}</span>
      </div>
      {/* Placeholder for future dropdown/selection UI */}
      {/* <select> <option>...</option> </select> */}
    </section>
  );
}

export default ChefSelector;