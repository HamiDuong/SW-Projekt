import {
    DialogContent,
    TextField,
    Dialog,
    DialogTitle,
    DialogActions,
    Button
} from '@mui/material';
import React, { Component } from 'react';


class CreateWorkTimeSheet extends Component {
    constructor(props) {
        super(props);
        this.state = {
            workbookings: props.workbookings,

            workTimeSheetWindow: false

        };
        this.basestate = this.state;
    }

    handleClose = () => {
        this.props.onClose(null)
    }

    // createTimeSheet = () => {
    //     //COde
    //     this.handleClose;
    // }

    render() { 
        const { classes, show } = this.props
        return (
            show ?
            <Dialog open = {show} onClose = {this.handleClose} maxWidth = 'xs'>
                <DialogContent>
                    <DialogTitle>
                        <h2>Create your Work Time Sheet</h2>
                    </DialogTitle>

                    <h3>Input the path where you want to save the file:</h3>

                    <TextField
                        id = "path"
                        label="Data Path"
                        variant = "standard"
                        defaultValue={this.state.booking.start}
                        InputLabelProps={{
                        shrink: true,
                        }}
                    >
                    </TextField>
                </DialogContent>
                <DialogActions>
                    <Button
                        onClick={this.handleClose}
                    >
                        Cancel
                    </Button>
                    <Button
                        onClick={this.createTimeSheet}
                    >
                        Create Work Time Sheet
                    </Button>
                </DialogActions>
            </Dialog>
            : null
        );
    }
}
 
export default CreateWorkTimeSheet;