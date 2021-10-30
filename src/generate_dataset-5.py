import pandas as pd
import os


# Load data
plavki_train = pd.read_csv('data/raw/plavki_train.csv', index_col='NPLV')
plavki_test = pd.read_csv('data/raw/plavki_test.csv', index_col='NPLV')


chugun_train  = pd.read_csv('data/raw/chugun_train.csv', index_col='NPLV')
chugun_test  = pd.read_csv('data/raw/chugun_test.csv', index_col='NPLV')
chugun_train = chugun_train.add_prefix('chugun_')
chugun_test = chugun_test.add_prefix('chugun_')

sip_train = pd.read_csv('data/raw/sip_train.csv')
sip_test = pd.read_csv('data/raw/sip_test.csv')

chronom_train = pd.read_csv('data/raw/chronom_train.csv', index_col=0, parse_dates=['VR_NACH', 'VR_KON'])
chronom_test = pd.read_csv('data/raw/chronom_test.csv', index_col=0, parse_dates=['VR_NACH', 'VR_KON'])

lom_train = pd.read_csv('data/raw/lom_train.csv')
lom_test = pd.read_csv('data/raw/lom_test.csv')

produv_train = pd.read_csv('data/raw/produv_train.csv')
produv_test = pd.read_csv('data/raw/produv_test.csv')

gas_train = pd.read_csv('data/raw/gas_train.csv')
gas_test = pd.read_csv('data/raw/gas_test.csv')

lom_train = pd.read_csv('data/raw/lom_train.csv')
lom_test = pd.read_csv('data/raw/lom_test.csv')

target_train = pd.read_csv('data/raw/target_train.csv', index_col='NPLV')

sample_submission = pd.read_csv('data/raw/sample_submission.csv', index_col='NPLV')


# drop many plavk
mask = (plavki_train.index == 511135) & (plavki_train['plavka_ST_FURM'] != 46)
plavki_train = plavki_train[~mask]

# lom
lom_train = lom_train.drop(columns='NML')
lom_test = lom_test.drop(columns='NML')

lom_train = pd.pivot(lom_train, index='NPLV', columns='VDL', values='VES').fillna(0).astype(int).add_prefix('lom_VES_VLD')
lom_test = pd.pivot(lom_test, index='NPLV', columns='VDL', values='VES').fillna(0).astype(int).add_prefix('lom_VES_VLD')

lom_train['lom_components'] = lom_train.apply(lambda x: (x > 0).sum(), axis=1)
lom_test['lom_components'] = lom_test.apply(lambda x: (x > 0).sum(), axis=1)
# remove 1 column
lom_train = lom_train[lom_test.columns]

# sip
sip_train = sip_train.drop(columns=['NMSYP', 'DAT_OTD'])
sip_test = sip_test.drop(columns=['NMSYP', 'DAT_OTD'])
sip_train = sip_train.groupby(['NPLV', 'VDSYP'])['VSSYP'].sum().reset_index()
sip_test = sip_test.groupby(['NPLV', 'VDSYP'])['VSSYP'].sum().reset_index()
sip_train = pd.pivot(sip_train, index='NPLV', columns='VDSYP', values='VSSYP').fillna(0).astype(int).add_prefix('sip_VES_VDSYP')
sip_test = pd.pivot(sip_test, index='NPLV', columns='VDSYP', values='VSSYP').fillna(0).astype(int).add_prefix('sip_VES_VDSYP')
# Remove columns
sip_test = sip_test[sip_train.columns]

sip_train['sip_components'] = sip_train.apply(lambda x: (x > 0).sum(), axis=1)
sip_test['sip_components'] = sip_test.apply(lambda x: (x > 0).sum(), axis=1)


# produv_train
min_pol_train = produv_train.groupby('NPLV')['POL'].min().to_frame().add_prefix('produv_min_')
mean_pol_train = produv_train.groupby('NPLV')['POL'].mean().to_frame().add_prefix('produv_mean_')
max_pol_train = produv_train.groupby('NPLV')['POL'].max().to_frame().add_prefix('produv_max_')

min_pol_test = produv_test.groupby('NPLV')['POL'].min().to_frame().add_prefix('produv_min_')
mean_pol_test = produv_test.groupby('NPLV')['POL'].mean().to_frame().add_prefix('produv_mean_')
max_pol_test = produv_test.groupby('NPLV')['POL'].max().to_frame().add_prefix('produv_max_')

ras_train = produv_train.groupby('NPLV')['RAS'].sum().to_frame().add_prefix('produv_sum_')
ras_test = produv_test.groupby('NPLV')['RAS'].sum().to_frame().add_prefix('produv_sum_')

ras_train_mean = produv_train.groupby('NPLV')['RAS'].mean().to_frame().add_prefix('produv_mean_')
ras_test_mean = produv_test.groupby('NPLV')['RAS'].mean().to_frame().add_prefix('produv_mean_')

produv_train_groupped = pd.concat([max_pol_train, mean_pol_train, min_pol_train, ras_train_mean, ras_train], axis=1)
produv_test_groupped = pd.concat([max_pol_test, mean_pol_test, min_pol_test, ras_test_mean, ras_test], axis=1)


# gas_train
gas_train = gas_train.drop(columns='Time')
gas_test = gas_test.drop(columns='Time')

_gas_train = gas_train.groupby(['NPLV']).agg(
    {
        'V':['mean', 'sum'],
        'T':['mean', 'sum'],
        'O2':['mean', 'sum'],
        'N2':['mean', 'sum'],
        'H2':['mean', 'sum'],
        'CO2':['mean', 'sum'],
        'CO':['mean', 'sum'],
        'AR':['mean', 'sum'],
        'T фурмы 1':['mean', 'sum'],
        'T фурмы 2':['mean', 'sum'],
        'O2_pressure':['mean', 'sum'],
    })
_gas_train.columns = ["_".join(x) for x in _gas_train.columns.ravel()]

_gas_test = gas_test.groupby(['NPLV']).agg(
    {
        'V':['mean', 'sum'],
        'T':['mean', 'sum'],
        'O2':['mean', 'sum'],
        'N2':['mean', 'sum'],
        'H2':['mean', 'sum'],
        'CO2':['mean', 'sum'],
        'CO':['mean', 'sum'],
        'AR':['mean', 'sum'],
        'T фурмы 1':['mean', 'sum'],
        'T фурмы 2':['mean', 'sum'],
        'O2_pressure':['mean', 'sum'],
    })
_gas_test.columns = ["_".join(x) for x in _gas_test.columns.ravel()]


gas_train = _gas_train.add_prefix('gas_')
gas_test = _gas_test.add_prefix('gas_')

## chronom_train
chronom_train['operation_time'] = (chronom_train['VR_KON'] - chronom_train['VR_NACH']).dt.total_seconds()
chronom_test['operation_time'] = (chronom_test['VR_KON'] - chronom_test['VR_NACH']).dt.total_seconds()

chronom_train = chronom_train.groupby(['NPLV', 'NOP'])['operation_time'].mean().reset_index()
chronom_test = chronom_test.groupby(['NPLV', 'NOP'])['operation_time'].mean().reset_index()

chronom_train = pd.pivot(chronom_train, index='NPLV', columns='NOP', values='operation_time').fillna(0).astype(int)
chronom_test = pd.pivot(chronom_test, index='NPLV', columns='NOP', values='operation_time').fillna(0).astype(int)

common_columns = [x for x in chronom_test.columns if x in chronom_train.columns]

chronom_train = chronom_train[common_columns]
chronom_test = chronom_test[common_columns]

chronom_train = chronom_train.add_prefix('chronom_time_')
chronom_test = chronom_test.add_prefix('chronom_time_')

# Merge
train = pd.merge(target_train, chugun_train, left_index=True, right_index=True, how='outer')
train = pd.merge(train, plavki_train, left_index=True, right_index=True, how='outer')
train = pd.merge(train, lom_train, left_index=True, right_index=True, how='outer')
train = pd.merge(train, sip_train, left_index=True, right_index=True, how='outer')
train = pd.merge(train, produv_train_groupped, left_index=True, right_index=True, how='outer')
train = pd.merge(train, gas_train, left_index=True, right_index=True, how='outer')
train = pd.merge(train, chronom_train, left_index=True, right_index=True, how='outer')

print("Nas:", train.isna().sum().sum())
print("Shape:", train.shape)

test = pd.merge(sample_submission, chugun_test, left_index=True, right_index=True, how='outer')
test = pd.merge(test, plavki_test, left_index=True, right_index=True, how='outer')
test = pd.merge(test, lom_test, left_index=True, right_index=True, how='outer')
test = pd.merge(test, sip_test, left_index=True, right_index=True, how='outer')
test = pd.merge(test, produv_test_groupped, left_index=True, right_index=True, how='outer')
test = pd.merge(test, gas_test, left_index=True, right_index=True, how='outer')
test = pd.merge(test, chronom_test, left_index=True, right_index=True, how='outer')

print("Nas:", test.isna().sum().sum())
print("Shape:", test.shape)


# Feature generation
train = pd.read_csv('data/processed/train.csv', parse_dates=['chugun_DATA_ZAMERA', 'plavka_VR_NACH', 'plavka_VR_KON']).dropna()
test = pd.read_csv('data/processed/test.csv', parse_dates=['chugun_DATA_ZAMERA', 'plavka_VR_NACH', 'plavka_VR_KON'])

train['chugun_DATA_ZAMERA'] = pd.to_datetime(train['chugun_DATA_ZAMERA'])
train['plavka_VR_NACH'] = pd.to_datetime(train['plavka_VR_NACH'])
train['plavka_VR_KON'] = pd.to_datetime(train['plavka_VR_KON'])

test['chugun_DATA_ZAMERA'] = pd.to_datetime(test['chugun_DATA_ZAMERA'])
test['plavka_VR_NACH'] = pd.to_datetime(test['plavka_VR_NACH'])
test['plavka_VR_KON'] = pd.to_datetime(test['plavka_VR_KON'])

train['timer'] = (train['chugun_DATA_ZAMERA'] - train['plavka_VR_NACH']).dt.total_seconds()
test['timer'] = (test['chugun_DATA_ZAMERA'] - test['plavka_VR_NACH']).dt.total_seconds()

train['VES/O2'] = train['chugun_VES'] / train['gas_O2_sum']
test['VES/O2'] = test['chugun_VES'] / test['gas_O2_sum']


train.to_csv('data/processed/train.csv')
test.to_csv('data/processed/test.csv')