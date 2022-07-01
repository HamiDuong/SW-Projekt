import React, { Component } from 'react';
import WatchLaterIcon from '@mui/icons-material/WatchLater';
class WelcomePage extends Component {
    constructor(props) {
        super(props);
    }
    state = {  }
    render() { 
        return ( 
        <div style={{width: ''}}>
            <h1 style={{textAlign:'center',
                fontFamily: 'monospace'}} >
                Welcome to our Worktimeapp!
            </h1>
            <WatchLaterIcon style={{
                width: 60,
                height: 60,
                marginRight: 'auto',
                marginLeft: 'auto',
                display: 'flex',
                alignItems: 'center',
                flexWrap: 'wrap',
                color: 'purple'
            }}/>
        </div>
        );
    }
}
 
export default WelcomePage;