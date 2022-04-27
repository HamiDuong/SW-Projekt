import React, { Component } from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import EventIcon from '@mui/icons-material/Event';
import Grid from '@mui/material/Grid'
import Card from '@mui/material/Card';
import Typography from '@mui/material/Typography';
import FormControl from '@mui/material/FormControl';



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
            <Card sx={{ m:5, p:2, minwidth: 500}}>
              <Grid container spacing={2} sx={{mb:2}} direction="row" alignItems="center">
                        <Grid item  sx={{border: 1, borderRadius: 4, ml:2, p:2}}>
                            <Grid item >
                                <EventIcon></EventIcon>
                            </Grid>
                        </Grid>
                        <Grid item xs={12} sm={4} sx={{pb:1}}>
                            <Typography variant="h5" component="div">
                            Create Your Event Booking
                            </Typography>
                            <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                            Please fill out all relevant information. 
                            </Typography>
                        </Grid>
                </Grid>
                <Grid container spacing={2}  alignItems="center">
                  <Grid item xs={12}>
                       <FormControl sx={{ minWidth: 220}}>
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
                        </FormControl>
                      </Grid>
                      <Grid item xs={4} sm={2}>
                      <TextField name="date" label="Date" variant="outlined" />
                      </Grid>
                      <Grid item xs={4} sm={10}>
                      <TextField name="time" label="Time" variant="outlined" />
                      </Grid>
                      <Grid item xs={4} sm={2}>
                      <Button variant="contained">Book Event</Button>
                      </Grid>
              </Grid>
          </Card>
         );
    }
}
 
export default EventBookings;