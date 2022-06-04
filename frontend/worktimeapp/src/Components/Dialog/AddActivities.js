import React, { Component } from 'react';

class AddActivities extends Component {
    constructor(props) {
        super(props);
    }
    state = {  }
    render() { 
        return ( 
            <div className='popup'>
                <div className='popup_inner'>
                <h1>{this.props.text}</h1>
                <button onClick={this.props.closePopup}>close me</button>
                </div>
            </div>
         );
    }
}
 
export default AddActivities;