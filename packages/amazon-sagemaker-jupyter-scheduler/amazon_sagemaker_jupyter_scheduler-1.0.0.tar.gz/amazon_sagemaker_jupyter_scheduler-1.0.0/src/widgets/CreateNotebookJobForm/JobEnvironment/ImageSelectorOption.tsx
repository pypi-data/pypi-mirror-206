import React from 'react';

import { i18nStrings } from '../../../constants';
import { Link, LinkTarget } from '../../../components/link';
import {
  imageDropdownDescContainer,
  imageDropdownOptionDesc,
  imageDropdownOptionLabel,
  imageDropdownOptionLink,
} from './styles';

//TODO: Import MUI Link, Icon,  component here see if we need add any new props to what we have today in SWA
// DropdownItem ref: https://github.com/aws/sagemaker-ui/blob/master/packages/sagemaker-ui-components/src/components/Dropdown/Component.tsx
const ImageSelectorOption = (option: any, selected?: boolean) => {
  return (
    <span>
      <div className={imageDropdownOptionLabel} data-selected={selected}>
        <p>{option.label}</p>
      </div>
      <div>{renderLinkInDescription(option.optionMetadata && option.optionMetadata.description)}</div>
    </span>
  );
};

const renderLinkInDescription = (description: string): React.ReactFragment | undefined => {
  if (!description) {
    return undefined;
  }
  const linkRegexExp = /(((https?:\/\/)|(www\.))[^\s]+)/g;
  const links = description.match(linkRegexExp);
  if (links) {
    for (const link of links) {
      description = description.replace(link, ' ');
    }
  }

  const trimmedDescription = description.trim();

  return (
    <div className={imageDropdownDescContainer}>
      <span className={imageDropdownOptionDesc}>{trimmedDescription}</span>
      {links &&
        links.map((link) => (
          <Link className={imageDropdownOptionLink} key={link} href={link} target={LinkTarget.External}>
            {i18nStrings.KernelSelector.imageSelectorOption.linkText}
          </Link>
        ))}
    </div>
  );
};

export { ImageSelectorOption };
