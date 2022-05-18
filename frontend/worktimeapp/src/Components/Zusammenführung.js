import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import InputLabel from '@mui/material/InputLabel';
import OutlinedInput from '@mui/material/OutlinedInput';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

function createData(name, activities, plannedTime, bookedTime, employee) {
    return { name, activities, plannedTime, bookedTime, employee };
}


const rows = [
    createData('Project A', 'Use Case erstellen', 15, 6.0, ['Max Mustermann ', 'Hannah']),
    createData('Project A', 'Malen', 23, 9.0, ['Max Mustermann ', 'Hannah']),
    createData('Project A', 'Basteln', 22, 16.0, ['Max Mustermann ', 'Hannah']),
    createData('Project A', 'React hassen', 35, 3.7, ['Max Mustermann ', 'Hannah']),
    createData('Project A', 'Mann oh MANN', 56, 16.0, ['Max Mustermann ', 'Hannah']),
];

export default function BasicTable() {
    const [open, setOpen] = React.useState(false);
    const [age, setAge] = React.useState('');

    const handleChange = (event) => {
        setAge(Number(event.target.value) || '');
    };

    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = (event, reason) => {
        if (reason !== 'backdropClick') {
            setOpen(false);
        }
    };
    return (
        <div>
            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 650 }} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell>Project</TableCell>
                            <TableCell align="right">Activites</TableCell>
                            <TableCell align="right">Planned Time&nbsp;(h)</TableCell>
                            <TableCell align="right">Booked Time&nbsp;(h)</TableCell>
                            <TableCell align="right">Employee</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {rows.map((row) => (
                            <TableRow
                                key={row.name}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            >
                                <TableCell component="th" scope="row">
                                    {row.name}
                                </TableCell>
                                <TableCell align="right">{row.activities}</TableCell>
                                <TableCell align="right">{row.plannedTime}</TableCell>
                                <TableCell align="right">{row.bookedTime}</TableCell>
                                <TableCell align="right">{row.employee}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
            <div>
                <Button onClick={handleClickOpen}>Open select dialog</Button>
                <Dialog disableEscapeKeyDown open={open} onClose={handleClose}>
                    <DialogTitle>Fill the form</DialogTitle>
                    <DialogContent>
                        <Box component="form" sx={{ display: 'flex', flexWrap: 'wrap' }}>
                            <FormControl sx={{ m: 1, minWidth: 120 }}>
                                <InputLabel htmlFor="demo-dialog-native">Age</InputLabel>
                                <Select
                                    native
                                    value={age}
                                    onChange={handleChange}
                                    input={<OutlinedInput label="Age" id="demo-dialog-native" />}
                                >
                                    <option aria-label="None" value="" />
                                    <option value={10}>Ten</option>
                                    <option value={20}>Twenty</option>
                                    <option value={30}>Thirty</option>
                                </Select>
                            </FormControl>
                            <FormControl sx={{ m: 1, minWidth: 120 }}>
                                <InputLabel id="demo-dialog-select-label">Age</InputLabel>
                                <Select
                                    labelId="demo-dialog-select-label"
                                    id="demo-dialog-select"
                                    value={age}
                                    onChange={handleChange}
                                    input={<OutlinedInput label="Age" />}
                                >
                                    <MenuItem value="">
                                        <em>None</em>
                                    </MenuItem>
                                    <MenuItem value={10}>Ten</MenuItem>
                                    <MenuItem value={20}>Twenty</MenuItem>
                                    <MenuItem value={30}>Thirty</MenuItem>
                                </Select>
                            </FormControl>
                        </Box>
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={handleClose}>Cancel</Button>
                        <Button onClick={handleClose}>Ok</Button>
                    </DialogActions>
                </Dialog>
            </div>
        </div>
    );
}
