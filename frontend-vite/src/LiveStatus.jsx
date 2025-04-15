import React from 'react';
import './LiveStatus.css'; // CSS file to be created next

// Define possible status values (could be imported from a constants file later)
const STATUS = {
  IDLE: 'idle',
  ORDERED: 'ordered',
  COOKING: 'cooking',
  DELIVERED: 'delivered',
  ERROR: 'error',
};

// Maps status to user-friendly text
const statusText = {
  [STATUS.ORDERED]: 'Order In!',
  [STATUS.COOKING]: 'Chef is Cooking You Something Awesome...',
  [STATUS.DELIVERED]: 'Your Order is Delivered! Bon Appétit!',
  [STATUS.ERROR]: 'Uh oh! There was a problem with the order.',
};

// Maps status to the step index for highlighting
const statusToIndex = {
  [STATUS.ORDERED]: 0,
  [STATUS.COOKING]: 1,
  [STATUS.DELIVERED]: 2,
  [STATUS.ERROR]: -1, // Special case for error
};

function LiveStatus({ status }) {
  // Don't render anything if idle
  if (status === STATUS.IDLE) {
    return null;
  }

  const activeIndex = statusToIndex[status] ?? -1; // Default to -1 if status unknown
  const steps = [statusText[STATUS.ORDERED], statusText[STATUS.COOKING], statusText[STATUS.DELIVERED]];

  return (
    <section className="live-status-section">
      <h2 className="section-title">Live Order Status</h2>
      {status === STATUS.ERROR ? (
        <div className="status-error">{statusText[STATUS.ERROR]}</div>
      ) : (
        <div className="status-tracker">
          {steps.map((text, index) => (
            <React.Fragment key={index}>
              <div
                className={`status-step ${index <= activeIndex ? 'active' : ''} ${index === activeIndex ? 'current' : ''}`}
              >
                <div className="step-number">{index + 1}</div>
                <div className="step-text">{text}</div>
              </div>
              {index < steps.length - 1 && <div className={`status-connector ${index < activeIndex ? 'active' : ''}`}></div>}
            </React.Fragment>
          ))}
        </div>
      )}
    </section>
  );
}

// Export STATUS constants for use in App.jsx
export { STATUS };
export default LiveStatus;