import React from 'react';

const SocietyInfo = (props) => {
    return (
        <div id="bottom-right">
            <div id="points-indicator">
                <span className="number">{props.score}</span>
                <span className="label">Society points</span>
            </div>
            <button id="edit-button">Edit page</button>
        </div>
    );
}

export default SocietyInfo;
