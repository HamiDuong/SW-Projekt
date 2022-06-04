import {
    DialogActions,
    TextField,
    Dialog,
    DialogContent,
    DialogTitle,
    Button
} from '@mui/material';
import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';

class EditBooking extends Component {
    constructor(props) {
        super(props);
        this.state = {
            booking: props.booking,

            startdate: null,
            enddate:null
        }
    }

    handleClose = () => {
        this.props.onClose(null)
    }
    
    deleteBooking = (obj) => {
        console.log("Booking löschen")
        // WorkTimeAppAPI.getAPI().deleteBooking(obj)

    }

    saveChanges = () => {
        console.log("Booking bearbeiten")

    }

    render() { 
        const { classes, show } = this.props
        return (
            show ?
            <Dialog open={show} onClose={this.handleClose} maxWidth='xs'>
                <DialogContent>
                    <DialogTitle>
                        <h2>Edit the booking</h2>
                    </DialogTitle>
                        <TextField
                            id = "startdate"
                            label="Start Date"
                            variant = "standard"
                            format={'YYYY/MM/DD'}
                            type = "date"
                            defaultValue={this.state.booking.start}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                        <TextField
                            id = "enddate"
                            label="End Date"
                            variant = "standard"
                            format={'YYYY/MM/DD'}
                            type = "date"
                            defaultValue={this.state.booking.end}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                </DialogContent>
                <DialogActions>
                    <Button
                        onClick={this.handleClose}
                    >
                        Cancel
                    </Button>
                    <Button
                        onClick={this.deleteBooking}
                    >
                        Delete
                    </Button>
                    <Button
                        onClick={this.saveChanges}
                    >
                        Edit
                    </Button>
                </DialogActions>
            </Dialog>
            : null
        );
    }
}
 
export default EditBooking;