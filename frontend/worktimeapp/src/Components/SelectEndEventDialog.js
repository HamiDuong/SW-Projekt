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
import Grid from '@mui/material/Grid';
import { Typography } from '@mui/material';

/* 
@author Mihriban Dogan (https://github.com/mihriban-dogan)
SelectEventDialog stellt stellt den Dialog für die Auswahl von End Events dar.
*/


class SelectEndEventDialog extends Component {
    constructor(props) {
        super(props);

        this.state = {
            
            endevent: Date


        }
    }
    
    handleClose = () => {
        this.props.onClose(null);
          }
          
    handleChange = (e) =>{
        this.setState({ [e.target.name] : e.target.value }, function(){
            console.log(this.state.event)
        } )}

    updateStart = () => {
        this.props.onClose(this.state.endevent)
    }


    render() { 
        return (
            <Dialog open={this.props.show} onClose={this.handleClose}>
                <DialogTitle>Select Event</DialogTitle>
                <DialogContent>
                <DialogContentText sx={{mb:2}}>
                Please select a desired event.
                </DialogContentText>
                    <Grid container spacing={2}>
                        <Grid xs={12} sm={6} item>
                    </Grid>

                    <Grid xs={12} sm={6} sx={{mb:2}} item>
                    </Grid>

                    <Grid  xs={12} item>

                    <FormControl sx={{ width: "100%"}}>
                            <InputLabel>Select Event</InputLabel>
                            <Select
                                name="endevent"
                                value={this.state.start}
                                label="Select Event"
                                onChange={this.handleChange}
                            >
                                {this.props.vacationIllnessEvents.map(vacationBOs =>
                                <MenuItem key={vacationBOs} value={vacationBOs}>
                                    <div>
                                    <Typography style={{fontWeight: "bold"}}> Type:</Typography> {vacationBOs.getType()}
                                    <Typography style={{fontWeight: "bold"}}> Time:</Typography>{vacationBOs.getTime()}
                                    </div>
                                </MenuItem>
                                )}
                            </Select>
                    </FormControl>
                    </Grid>
                    </Grid>
                </DialogContent>
                <DialogActions>
                <Button onClick={this.handleClose}>Cancel</Button>
                <Button onClick={this.updateStart}>Select</Button>
                </DialogActions>
        </Dialog>
          );
    }
}
 
export default SelectEndEventDialog;