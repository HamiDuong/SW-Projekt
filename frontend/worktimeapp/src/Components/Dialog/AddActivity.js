import { Dialog, DialogActions, DialogContent, DialogTitle, TextField, Button } from '@mui/material';
import React, {Component} from 'react';
import WorkTimeAPI from '../../API/WorkTimeAppAPI'
import ActivityBO from '../../API/ActivityBO'

/**
 * @author [Vi Nam Le] (https://github.com/vinamle)
 * 
 * Dialog um Aktivities zu bestehenden Projekten hinzuzufügen
 */
class AddActivity extends Component {
    constructor(props){
        super(props);
        this.state = {
            project : this.props.project,

            name : '',
            capacity : '',
            projectId : this.props.project,
            currentCapacity: 0
        }
    }

    // Änderungen im State abspeichern
    handleChange = (event) => {
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

    // Dialogfenster schließen
    handleClose = () => {
        this.props.onClose(null)
    }

    // erstellt ein neues ActivityBO mit den Daten aus State
    addActivity = () => {
        let activity = new ActivityBO(
            this.state.name,
            this.state.capacity,
            this.state.projectId,
            this.state.currentCapacity
        )
        WorkTimeAPI.getAPI().addActivity(activity).then(
            console.log(activity)
        );
        // this.handleClose();
        this.props.onClose(activity)
    }

    render() { 
        const { classes, show } = this.props
        const { name, capacity} = this.state
        return (
            show ?
            <Dialog open = {show} onClose = {this.handleClose}>
                <DialogContent>
                    <DialogTitle>
                        <h2>Add a activity</h2>
                    </DialogTitle>
                    <TextField
                        id="name"
                        label="Name"
                        variant="standard"
                        type = 'text'
                        value = {name}
                        onChange = {this.handleChange}
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <TextField
                        id="capacity"
                        label="Capacity"
                        variant="standard"
                        type = 'text'
                        value = {capacity}
                        onChange = {this.handleChange}
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
                        onClick={this.addActivity}
                    >
                        Add activity
                    </Button>
                </DialogActions>
            </Dialog>
            : null
        );
    }
}
 
export default AddActivity;