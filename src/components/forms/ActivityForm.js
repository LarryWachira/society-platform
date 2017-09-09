import React from 'react';

const ActivityForm = (props) => {
    return (
        <div>
            <table id="activity-form">
                <tbody>
                    <tr>
                        <td>
                            <span className="label">Select the activity</span>
                        </td>
                        <td>
                            <div>
                                <select name="name" value={props.name}
                                    onChange={props.onChange}>
                                    <option value="d">Organizing a tech event</option>
                                    <option value="e">Interviewing candidates for a fellow recruitment event</option>
                                </select>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span className="label">Quantity</span>
                        </td>
                        <td>
                            <div>
                                <input value={props.quantity}
                                onChange={props.onChange} name="quantity" type="number" />
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span className="label">Add comment</span>
                        </td>
                        <td>
                            <div>
                                <textarea value={props.comment}
                                    onChange={props.onChange} name="comment" type="text" />
                            </div>
                        </td>
                    </tr>

                    <tr>
                        <td colSpan="2" className="form-buttons">
                        <button id="cancel"
                            onClick={props.close}>Cancel</button>
                        <button id="submit"
                            onClick={props.addActivity}
                            disabled={props.isWorking}>Log</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    );
}

export default ActivityForm;
