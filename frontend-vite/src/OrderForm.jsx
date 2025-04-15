import React from 'react';
import './OrderForm.css'; // CSS file to be created next

// Receives prompt state and handlers from the parent (App.jsx)
function OrderForm({ prompt, onPromptChange, onSubmit }) {
  return (
    <section className="order-form-section">
      <h2 className="section-title">What Should the Chef Prepare for You?</h2>
      <div className="form-content">
        <textarea
          className="prompt-input"
          placeholder="Describe the MCP server or tool you'd like the Chef to create..."
          value={prompt}
          onChange={onPromptChange} // Use the handler passed via props
          rows="6" // Adjust rows as needed
        />
        <button
          className="submit-button"
          onClick={onSubmit} // Use the handler passed via props
        >
          Place Your Order
        </button>
      </div>
    </section>
  );
}

export default OrderForm;