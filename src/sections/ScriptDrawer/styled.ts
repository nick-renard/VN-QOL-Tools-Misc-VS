// Let's style the MUI drawer component
import { Drawer } from '@mui/material';

// We can use the styled function from MUI to style the drawer
// We can also use the styled function from @mui/system
// We will use the styled function from @mui/system
import { styled } from '@mui/system';

const StyledDrawer = styled(Drawer)({
    // The drawer will be positioned to the right of the screen
    // The drawer will be 100% of the height of the screen
    // The drawer will be 25% of the width of the screen
    width: '25%',
    height: '100%',
    position: 'relative'
});

// We can also style the drawer's paper component
// We can also use the styled function from @mui/system
// We will use the styled function from @mui/system
const StyledDrawerPaper = styled('div')({
    // The drawer's paper will be positioned to the right of the screen
    // The drawer's paper will be 100% of the height of the screen
    // The drawer's paper will be 25% of the width of the screen
    width: '25%',
    height: '100%',
    position: 'relative'
});

export { StyledDrawer, StyledDrawerPaper };