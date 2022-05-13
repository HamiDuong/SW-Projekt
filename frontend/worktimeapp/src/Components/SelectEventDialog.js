import React, { Component } from 'react';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import TextField from '@mui/material/TextField';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Grid from '@mui/material/Grid'


class SelectEventDialog extends Component {
    constructor(props) {
        super(props);

        this.state = {
            timeframestart: Date,
            timeframeend: Date,
            event: ""


        }
    }

    handleStartDateChange(newValue){
        this.setState({
            timeframestart: new Date(newValue)
        })
        console.log(this.state.start)
    }
    handleEndDateChange(newValue){
        this.setState({
            timeframeend: new Date(newValue)
        })
        console.log(this.state.end)
    }

    handleChange = (e) =>{
        this.setState({ [e.target.name] : e.target.value });}

    handleClose = () => {
        this.props.onClose(null);
          }
    

    render() { 
        return (
            <Dialog open={this.props.show} onClose={this.handleClose}>
                <DialogTitle>Select Event</DialogTitle>
                <DialogContent>
                <DialogContentText sx={{mb:2}}>
                    To select an event, please give in your desired time frame and choose an event from the drop-down list.
                </DialogContentText>
                    <Grid container spacing={2}>
                        <Grid xs={12} sm={6} item>
                    <LocalizationProvider dateAdapter={AdapterDateFns}>
                        <DateTimePicker
                        renderInput={(props) => <TextField {...props} />}
                        label="Timeframe Start"
                        value={this.state.timeframestart}
                        onChange={(newValue) => {
                        this.handleStartDateChange(newValue);
                        }}
                        minDate={new Date('2022-01-01')}
                        />
                    </LocalizationProvider>
                    </Grid>

                    <Grid xs={12} sm={6} sx={{mb:2}} item>

                    <LocalizationProvider dateAdapter={AdapterDateFns}>
                        <DateTimePicker
                        renderInput={(props) => <TextField {...props} />}
                        label="Timeframe End"
                        value={this.state.timeframeend}
                        onChange={(newValue) => {
                        this.handleEndDateChange(newValue);
                        }}
                        minDate={new Date('2022-01-01')}
                        />
                    </LocalizationProvider>
                    </Grid>

                    <Grid  xs={12} item>

                    <FormControl sx={{ width: "100%"}}>
                            <InputLabel>Select Event</InputLabel>
                            <Select
                                name="start"
                                value={this.state.start}
                                label="Select Event"
                                onChange={this.handleChange}
                            >
                                <MenuItem value={"event"}>TBD</MenuItem>
                            </Select>
                    </FormControl>
                    </Grid>
                    </Grid>
                </DialogContent>
                <DialogActions>
                <Button onClick={this.handleClose}>Cancel</Button>
                <Button >Select</Button>
                </DialogActions>
        </Dialog>
          );
    }
}
 
export default SelectEventDialog;