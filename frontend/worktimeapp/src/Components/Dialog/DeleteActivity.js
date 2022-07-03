import React, { Component } from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';

/**
 * @author Mihriban Dogan (https://github.com/mihriban-dogan)
 * Dialog zum löschen von Aktivitäten
 */
class DeleteActivity extends Component {
    constructor(props) {
        super(props);
    }

    

    deleteActivity = () => {
      WorkTimeAppAPI.getAPI().deleteActivity(this.props.activity);
      this.props.onClose(this.props.activity);

    }

    handleClose = () => {
        this.props.onClose(null);
      }
    

    render() { 
        return (
            <Dialog open={this.props.show} onClose={this.handleClose}>
              <DialogTitle >{"Do you really want to delete your activity?"}</DialogTitle>
              <DialogContent>
                <DialogContentText >
                If you click delete, your activity will be deleted.</DialogContentText>
              </DialogContent>
              <DialogActions>
                <Button color="primary" onClick={this.handleClose} >
                 Cancel
                </Button>
                <Button color="primary" onClick={this.deleteActivity} autoFocus>
                  Delete
                </Button>
              </DialogActions>
            </Dialog>
          );
    }
}
 
export default DeleteActivity;