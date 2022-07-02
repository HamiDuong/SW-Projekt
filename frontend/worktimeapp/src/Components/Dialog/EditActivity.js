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
import ActivityBO from '../../API/ActivityBO';

//Hier kommt Esras Fenster mit Start Stop für Activities rein

class EditActivity extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activity : props.activity,
            name : props.activity.name,
            capacity : props.activity.capacity
        };
        this.baseState = this.state;
    }

    handleChange = ev => {
        this.setState({ [ev.target.name]: ev.target.value });
    };

    textFieldValueChange = (event) => {
        const value = event.target.value;
    
        let error = false;
        if (value.trim().length === 0) {
          error = true;
        }
    
        this.setState({
          [event.target.id]: event.target.value,
          [event.target.id + 'ValidationFailed']: error,
          [event.target.id + 'Edited']: true
        });
    }

    editActivity = () => {
        let updatedActivity = Object.assign(new ActivityBO(), this.state.activity);
        updatedActivity.setName(this.state.name);
        updatedActivity.setCapacity(this.state.capacity);

        WorkTimeAppAPI.getAPI().updateActivity(updatedActivity).then(
            console.log(updatedActivity)
        )
        // this.handleClose()
        this.props.onClose(updatedActivity)
    }

    handleClose = () => {
        this.props.onClose(null);
      }


    render() { 
        const { classes, show } = this.props
        const { name, capacity} = this.state
        return (
            show ?
            <Dialog open={show} onClose={this.handleClose} maxWidth='xs'>
                <DialogContent>
                    <DialogTitle>
                        <h2>Edit Activity</h2>
                    </DialogTitle>
                        <TextField
                            id = "name"
                            label="Name"
                            variant="standard"
                            value = {name}
                            onChange = {this.textFieldValueChange}
                        />
                        <TextField
                            id = "capacity"
                            label="Capacity"
                            variant="standard"
                            value = {capacity}
                            onChange = {this.textFieldValueChange}
                        />
                </DialogContent>
                <DialogActions>
                    <Button
                        onClick={this.handleClose}
                    >
                        Cancel
                    </Button>
                    
                    <Button
                        onClick = {this.editActivity}
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