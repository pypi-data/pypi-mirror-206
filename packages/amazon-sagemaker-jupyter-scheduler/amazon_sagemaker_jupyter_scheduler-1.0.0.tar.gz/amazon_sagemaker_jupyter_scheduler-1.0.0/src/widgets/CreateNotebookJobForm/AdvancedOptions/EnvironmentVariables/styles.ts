import { css } from '@emotion/css';

export const EnvironmentVariablesContainer = css`
  display: flex;
  align-items: center;
  padding-right: 1em;
`;

export const EnvironmentVariableContainer = css`
  display: flex;
  flex-direction: column;
`;

export const EnvironmentVariablesInput = css`
  width: 170px;
`;

export const InputContainer = css`
  display: flex;
  flex-direction: column;
  margin-bottom: var(--jp-padding-large);
`;

export const InputLabel = css`
  height: 18px;
  margin-bottom: var(--jp-padding-small);
`;

//Setting one off font-size to make it fit better inline in form.Re-visit to handle button better in future
export const ConfigBtn = css`
  background-color: var(--jp-brand-color1);
  font-size: var(--jp-ui-font-size1);
  text-transform: none;
`;

export const Value = css`
  margin-left: 1em;
`;

export const tooltipsContainer = css`
  display: inline-flex;
  svg {
    width: 0.75em;
    height: 0.75em;
    transform: translateY(-2px);
  }
`;
