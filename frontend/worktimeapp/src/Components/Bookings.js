import React, { Component } from 'react';
import Box from '@mui/material/Box';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import EventIcon from '@mui/icons-material/Event';

class Bookings extends Component {
    constructor(props) {
        super(props);
       
        this.state = { 
          value: 0
         }
    }
   
    
    handleChange(newValue) {
      this.setState({
        value: newValue
      }) 
      console.log(this.state.value)
    }
    
    render() { 
        return (  
        <Box sx={{ width: 500 }}>
            <BottomNavigation 
            showLabels 
            value={this.state.value}
            onChange={(event, newValue) => this.handleChange(newValue)} >
              <BottomNavigationAction label="Events" icon={<EventIcon />}/>
              <BottomNavigationAction label="Timeintervals" icon={<AccessTimeIcon/>} />
            </BottomNavigation>
          </Box> );
    }
}
 
export default Bookings;

