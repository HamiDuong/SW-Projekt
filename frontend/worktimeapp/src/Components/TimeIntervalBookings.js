import React, { Component } from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';


class TimeIntervalBookings extends Component {
    constructor(props) {
        super(props);
       
        this.state = { 
            start: "",
            end: "",
            timeIntervalType: "",
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
                name="timeIntervalType"
                value={this.state.timeIntervalType}
                label="type"
                onChange={this.handleChange}
              >
                <MenuItem value={"work"}>Work</MenuItem>
                <MenuItem value={"project"}>Project</MenuItem>
                <MenuItem value={"vacation"}>Vacation</MenuItem>
                <MenuItem value={"illness"}>Illness</MenuItem>
                <MenuItem value={"flexday"}>Flexday</MenuItem>
              </Select>
              <TextField name="startdate" label="Start date" variant="outlined" />
              <TextField name="enddate" label="End date" variant="outlined" />
              <TextField name="starttime" label="Start time" variant="outlined" />
              <TextField name="endtime" label="End time" variant="outlined" />
              <Button variant="contained">Select Event</Button>
              <Button variant="contained">Select Event</Button>
              <Button variant="contained">Select Activity</Button>
              <Button variant="contained">Book Timeinterval</Button>
            </FormControl>
          </Box>
         );
    }
}
 
export default TimeIntervalBookings;