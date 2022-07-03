import React, { Component } from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';
import firebase from 'firebase/app';
import {signOut } from "firebase/auth";
import {auth} from '../firebaseConfig.js';


/**
 * @author Mihriban Dogan (https://github.com/mihriban-dogan)
 * Dialog zum löschen von Profilen
 */
class DeleteProfile extends Component {
    constructor(props) {
        super(props);
    }

    

    deleteUser = () => {
      WorkTimeAppAPI.getAPI().deleteUser(this.props.currentUser)
      this.props.onClose()
      signOut(auth)

    }

    

    render() { 
        return (
            <Dialog open={this.props.show} onClose={this.handleClose}>
              <DialogTitle >{"Do you really want to delete your profile and account?"}</DialogTitle>
              <DialogContent>
                <DialogContentText >
                If you click delete, your account will be permanently deleted from the Worktimeapp.</DialogContentText>
              </DialogContent>
              <DialogActions>
                <Button color="primary" onClick={this.props.onClose} >
                 Cancel
                </Button>
                <Button color="primary" onClick={this.deleteUser} autoFocus>
                  Delete
                </Button>
              </DialogActions>
            </Dialog>
          );
    }
}
 
export default DeleteProfile;