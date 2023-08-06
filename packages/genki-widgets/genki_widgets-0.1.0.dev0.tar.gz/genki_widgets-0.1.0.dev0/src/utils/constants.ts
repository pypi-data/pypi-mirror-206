import { EAutoRange } from 'scichart/types/AutoRange';
import { ENumericFormat } from 'scichart/types/NumericFormat';
import type { INumericAxisOptions } from 'scichart/Charting/Visuals/Axis/NumericAxis';

export const MAX_BUFFER_SIZE: number = 10_000_000;

export const SCICHART_KEY: string = 'V3gyfcWvx2tED1xhIYN88PAOAm81mECeXG/On8Mi7AHRU7xNoqSI0bfdzg9WaZt678Vv1kBZgLQVg/vZ2NU5wjyCZQ9b9nfpizcAB7vyq/BzXd4o8dlfEFsYdY76WoGmO2uduY95Vo18Rugw6ahktztv/uCw9Qe3RTZ7azrj4DBkkANuc8dkGSvZ0cEmthYiMVgzKiBDCu9TzXAH92GZrnpFZaiCv3Syicy6cSys6Y2UJW4uz7SfPjn6ORbF4TIAUm7jcVy0+/PCekZEcYQbFWhxCXsq3UX9V4WDjQcwrTLd6NvLoKWQhjL4970FaOkM2OXrHdeERg5jyresNn3TDMTOIo1uSQdlnSd3si89Kw9v/6VcRU3wm6lUywsuONUi8IoMdowg5UAPdhbzCHrDX+rVNDHQS8YmOzCe3EGFh9CwzQAGxuteYDkqXEhJ7wlkosOfJqT+Q9jtWmVLbJEYrfSJ6EJ94RUCjPwjwjyKUbkiq9Rv5buUbNouUsNNJWiX7vBV8+pJWxYh3skUQcsVOyg4xXVvsNl3GPsORqXB2YU9ZPwcOzOQrEqeraA6KMZxFM/M5jJo7zsItA==';

export const default_axis_options: INumericAxisOptions = {
	useNativeText: true,
	isVisible: true,
	drawMajorBands: true,
	drawMinorGridLines: true,
	drawMinorTickLines: true,
	drawMajorTickLines: true,
	drawMajorGridLines: true,
	labelStyle: { fontSize: 8 },
	labelFormat: ENumericFormat.Decimal,
	labelPrecision: 0,
	autoRange: EAutoRange.Never
};
