import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';
import { styled } from '@mui/system';
import S4logo from './logos/S4.svg';

const HotKeysButton = styled(Button)(({ theme }) => ({
  height: 'fit-content',
  alignSelf: 'center',
  marginRight: theme.spacing(1),
  borderColor: theme.palette.text.disabled,
  '&:hover': {
    borderColor: theme.palette.text.disabled,
  },
  color: theme.palette.text.disabled,
}));

const ButtonGroups = styled(ButtonGroup)(({ theme }) => ({
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'space-between',
  alignItems: 'center',
  margin: theme.spacing(1),
}));

export { HotKeysButton, ButtonGroups };
