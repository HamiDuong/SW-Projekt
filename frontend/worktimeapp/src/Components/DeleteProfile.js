import React, { Component } from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';



class DeleteProfile extends Component {
    constructor(props) {
        super(props);
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
                <Button color="primary" onClick={this.deleteProfile} autoFocus>
                  Delete
                </Button>
              </DialogActions>
            </Dialog>
          );
    }
}
 
export default DeleteProfile;