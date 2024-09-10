from rest_framework.views import APIView, Response
from api.data_loader import df



class ConversationRate(APIView):
    """
    Returns the conversion rate for each customer_id, along with the highest and lowest conversion rates.
    """

    def get(self, request):

        df['conversion_rate'] = df['conversions'] / df['revenue']

        highest = df.loc[df['conversion_rate'].idxmax()]
        lowest = df.loc[df['conversion_rate'].idxmin()]

        highest_conversion_rate = highest['conversion_rate'] * 100
        lowest_conversion_rate = lowest['conversion_rate'] * 100

        return Response({
            'highest_conversion_rate': f"{highest_conversion_rate:.5f}%",
            'lowest_conversion_rate': f"{lowest_conversion_rate:.5f}%"
        })


class StatusDistribution(APIView):
    """
    Provides a summary of the distribution of status across different types and categories.
    This should include total revenue and conversions for each status.
    """
    def get(self, request):
        result = df.groupby(['status', 'type', 'category']).agg(
            total_revenue=('revenue', 'sum'),
            total_conversions=('conversions', 'sum')
        ).reset_index()

        status_distribution_result = result.groupby(['type', 'category']).apply(
            lambda x: {
                'statuses': x.set_index('status')[['total_revenue', 'total_conversions']].to_dict(orient='index')
            }
        ).reset_index(name='statuses').to_dict(orient='records')

        return Response(status_distribution_result)


class CategoryTypePerformance(APIView):
    """
    Returns the total revenue and conversions grouped by category and type. It should also highlight the top-performing category and type combination.
    """

    def get(self, request):
        performance = df.groupby(['type', 'category']).agg(
            total_revenue=('revenue', 'sum'),
            total_conversions=('conversions', 'sum')
        ).reset_index()

        best_performance = performance.loc[performance['total_conversions'].idxmax()]

        performance['best_performance'] = (performance['type'] == best_performance['type']) & \
                                          (performance['category'] == best_performance['category'])

        performance_result = performance.to_dict(orient='records')
        return Response(performance_result)


class FilteredAggregation(APIView):
    """
    Exposes aggregated data for rows where type is CONVERSION, returning the average revenue and conversions per customer_id.
    """
    def get(self, request):
        result = df[df['type'] == "CONVERSION"].groupby('customer_id').agg(
            avg_revenue=('revenue', 'mean'),
            avg_conversions=('conversions', 'mean')
        ).reset_index().to_dict(orient="records")
        return Response(result)