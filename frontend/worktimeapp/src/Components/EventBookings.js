import React, { Component } from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';




class EventBookings extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            eventType: "",
            selectedDate: Date()
        }
    }
    handleChange = (e) =>{
        this.setState({ [e.target.name] : e.target.value });}


    render() { 
        return ( 
            <Box sx={{ minWidth: 120 }}>
            <FormControl fullWidth>
              <InputLabel>Type</InputLabel>
              <Select
                name="eventType"
                value={this.state.eventType}
                label="Type"
                onChange={this.handleChange}
              >
                <MenuItem value={"Coming"}>Coming</MenuItem>
                <MenuItem value={"Going"}>Going</MenuItem>
              </Select>
              <TextField name="date" label="Date" variant="outlined" />
              <TextField name="time" label="Time" variant="outlined" />
              <Button variant="contained">Book Event</Button>
            </FormControl>
          </Box>
         );
    }
}
 
export default EventBookings;