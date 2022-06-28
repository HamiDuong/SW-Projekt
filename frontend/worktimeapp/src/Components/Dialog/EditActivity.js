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

//Hier kommt Esras Fenster mit Start Stop für Activities rein

class EditActivity extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activity: props.elem,
        };
        this.baseState = this.state;
    }

    handleClose = () => {
        this.props.onClose(null)
    }
    
    deleteBooking = (obj) => {
        console.log("Löschen")
    }

    render() { 
        const { classes, show } = this.props
        return (
            show ?
            <Dialog open={show} onClose={this.handleClose} maxWidth='xs'>
                <DialogContent>
                    <DialogTitle>
                        <h2>Edit Activity</h2>
                    </DialogTitle>
                        <TextField
                            id = "startdate"
                            label="Start Date"
                            variant = "standard"
                            format={'YYYY/MM/DD'}
                            type = "date"
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

                    >
                        Delete
                    </Button>
                    <Button

                    >
                        Edit
                    </Button>
                </DialogActions>
            </Dialog>
            : null
        );
    }
}
 
export default EditActivity;