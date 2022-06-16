import React, { Component } from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import { Typography } from '@mui/material';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import Dialog from '@mui/material/Dialog';
import DialogContent from '@mui/material/DialogContent';
import DialogActions from '@mui/material/DialogActions';
import DialogTitle from '@mui/material/DialogTitle';
import Box from '@mui/material/Box';
import UserBO from '../API/UserBO';
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';






class SelectEventDialog extends Component {
    constructor(props) {
        super(props);

        this.state = {
            firstName: "",
            lastName: ""
        }
        this.baseState = this.state;

    }

    
    handleClose = () => {
        this.props.onClose(null);
          }
          
    handleChange = (e) =>{
        this.setState({ [e.target.name] : e.target.value })}

    updateUser = () => {
        let updatedUserBO = Object.assign(new UserBO(), this.props.currentUser)
        updatedUserBO.setFirstName(this.state.firstName)
        updatedUserBO.setLastName(this.state.lastName)
        WorkTimeAppAPI.getAPI().updateUser(updatedUserBO)
        console.log(updatedUserBO)
        this.props.onClose(this.state.firstName, this.state.lastName, updatedUserBO)
        this.setState(this.baseState);

    }
   
    render() { 
        return (
            <Dialog open={this.props.show} sx={{p:5}} onClose={this.handleClose}>
                <DialogTitle>Edit your profile</DialogTitle>
                <DialogContent>
                    <Box m={2}>
                    <TextField onChange={this.handleChange} name="firstName" label="first name" value={this.state.firstName} variant="outlined" />
                    </Box>
                    <Box m={2}>
                    <TextField  onChange={this.handleChange} name="lastName" label="last name"value={this.state.lastName}  variant="outlined" />
                    </Box>
                    </DialogContent>
                    <DialogActions>
                    <Button variant="contained" color="error" onClick={this.props.onClose}>Cancel</Button>
                    <Button variant="contained" onClick={this.updateUser}>Edit </Button>
                    </DialogActions>
            </Dialog>
          );
    }
}
 
export default SelectEventDialog;