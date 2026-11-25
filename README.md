# Data Aike

Regional data storytelling initiative focused on Santa Cruz, Patagonia, Argentina. The project combines quantitative analysis, editorial visualizations and short-form audiovisual communication.

## Stories

- [Santa Cruz demographic analysis](https://github.com/gastonchalub/santa-cruz-demographic-analysis): departmental population projections and selected age-group comparisons.
- [Santa Cruz livestock forecast](https://github.com/gastonchalub/santa-cruz-livestock-forecast): historical sheep inventories and exploratory time-series forecasting.

## Editorial workflow

Source verification → data cleaning → exploratory analysis → statistical validation → scriptwriting → visual design → narration → video editing → publication.

## Visual principles

Vertical 9:16 composition, high-contrast typography, dynamic but readable motion, explicit units and dates, and clear separation between observed figures and projections. Forecast uncertainty and source provenance must remain visible.

## Example

The included script generates a vertical PNG chart from the recovered sheep-stock series. It is a new illustrative implementation, not the original video renderer. Run:

```bash
pip install -r requirements.txt
python src/story_chart.py
```

The original reels, narration, maps and animation source files have not been recovered and are not included. The example has not been executed as part of this release.
