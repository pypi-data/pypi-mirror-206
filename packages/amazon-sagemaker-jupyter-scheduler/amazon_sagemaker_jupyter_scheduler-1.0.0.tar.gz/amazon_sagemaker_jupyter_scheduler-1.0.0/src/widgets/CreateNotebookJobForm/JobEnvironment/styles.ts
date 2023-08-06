import { css } from '@emotion/css';

export const JobEnvironmentContainer = css`
  display: flex;
  flex-direction: column;
  padding: 10px;
`;

export const KernelImageSelectorContainer = css`
  display: flex;
  flex-direction: column;
`;

export const ImageSelector = css`
  margin-left: 10px;
`;

export const ValidationMessageStyled = css`
  font-size: calc(var(--bl-size-m) + var(--bl-size-s));
`;

export const ErrorIconStyled = css`
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin-top: calc(var(--bl-size-xs) + var(--bl-size-xs));
  gap: 0.5rem;
  svg {
    width: calc(var(--bl-size-m) + var(--bl-size-s));
    height: calc(var(--bl-size-m) + var(--bl-size-s));
    path {
      fill: var(--bl-color-root-red-400);
    }
  }
`;

export const imageDropdownDescContainer = css`
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-between;
  align-items: center;
`;

export const imageDropdownOptionLink = css`
  font-size: var(--jp-ui-font-size0);
  min-width: max-content;
`;

export const imageDropdownOptionDesc = css`
  font-size: var(--jp-ui-font-size0);
  color: var(--jp-inverse-layout-color4);
  padding-right: 5px;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
`;

export const imageDropdownOptionLabel = css`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  &[data-selected='true'] {
    background-image: var(--jp-check-icon);
    background-size: 15px;
    background-repeat: no-repeat;
    background-position: 100% center;
  }
  & > p {
    max-width: calc(100% - 10px);
  }
`;
