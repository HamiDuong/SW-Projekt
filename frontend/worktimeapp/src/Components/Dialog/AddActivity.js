import { Dialog, DialogActions, DialogContent, DialogTitle, TextField, Button } from '@mui/material';
import React, {Component} from 'react';
import WorkTimeAPI from '../../API/WorkTimeAppAPI'
import ActivityBO from '../../API/ActivityBO'

class AddActivity extends Component {
    constructor(props){
        super(props);
        this.state = {
            project : props.project,

            name : '',
            capacity : '',
            projectId : props.project.id,
            currentCapacity: 0
        }
    }

    handleChange = ev => {
        this.setState({
            [ev.target.name] : ev.target.value
        });
    }

    //speichert Änderungen in den Textfeldern in State
    handleClose = () => {
        this.props.onClose(null)
    }

    //erstellt ein neues ActivityBO mit den Daten aus State
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
    }

    render() { 
        const { classes, show } = this.props
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
                        
                        onChange = {this.handleChange}
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <TextField
                        id="capacity"
                        label="Capacity"
                        variant="standard"
                        
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