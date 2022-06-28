import {
    DialogContent,
    TextField,
    Dialog,
    DialogTitle,
    DialogActions,
    Button,
    TableContainer,
    Table,
    TableHead,
    TableBody,
    TableRow,
    TableCell
} from '@mui/material';
import React, { Component } from 'react';


class CreateWorkTimeSheet extends Component {
    constructor(props) {
        super(props);
        this.state = {
            workbookings: props.workbookings,
            showTable: false, 

            workTimeSheetWindow: false

        };
        this.basestate = this.state;
    }

    handleClose = () => {
        this.props.onClose(null)
    }

    componentDidMount(){
        //get Contract Time of current User
        //get Worktimeaccount by user id
        //get contract time
    }

    createTimeSheet = () => {
        let bookings = this.state.workbookings;
        return(
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell
                            key = 'date'
                        >Date</TableCell>
                        <TableCell
                            key = 'coming'
                        >Coming</TableCell>
                        <TableCell
                            key = 'going'
                        >Going</TableCell>
                        <TableCell
                            key = 'workedTime'
                        >Worked Time</TableCell>
                        <TableCell
                            key = 'contractTime'
                        >Contract Time</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {
                        this.state.workbookings.map( row =>
                            <TableRow>
                                <TableCell>
                                    {row.start}
                                </TableCell>
                                <TableCell>
                                    {row.start}
                                </TableCell>
                                <TableCell>
                                    {row.end}
                                </TableCell>
                                <TableCell>
                                    {row.end - row.start}
                                </TableCell>

                            </TableRow>
                        )
                    }
                </TableBody>
            </Table>
        )

    }

    render() { 
        const { classes, show } = this.props
        return (
            show ?
            <Dialog open={show} onClose={this.handleClose} maxWidth='s'>
                <DialogContent>
                    <DialogTitle>
                        <h2>Create your Work Time Sheet</h2>
                    </DialogTitle>

                    <h3>Input the path where you want to save the file:</h3>

                    <TextField
                        id = "path"
                        label="Data Path"
                        variant = "standard"
                        InputLabelProps={{
                        shrink: true,
                        }}
                    >
                    </TextField>
                    <>
                    {/* <TableContainer>
                        <this.createTimeSheet></this.createTimeSheet>
                    </TableContainer> */}
                        
                    </>
                </DialogContent>
                <DialogActions>
                    <Button
                        onClick={this.handleClose}
                    >
                        Cancel
                    </Button>
                    <Button
                        onClick={this.handleClose}
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