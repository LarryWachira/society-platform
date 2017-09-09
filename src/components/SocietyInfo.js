import React from 'react';

const SocietyInfo = (props) => {
    return (
        <div id="bottom-left">
            <div id="badge-wrapper" className="left">
                <img src={props.badge} alt="Badge" />
            </div>
            <div id="society-info" className="left">
                <span id="society-name">{props.name}</span>
                <p id="society-statement">{props.statement}</p>
            </div>
        <div className="clearfix"></div>
    </div>
    );
}

export default SocietyInfo;
